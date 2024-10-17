# IT - Venator

### Descrizione

Venator è uno script Python utilizzato per eseguire azioni di persistence e bypass delle difese su un sistema Windows. Questo script scarica ed esegue un payload malevolo, crea un servizio per la persistenza, e tenta di terminare alcuni processi noti di EDR (Endpoint Detection and Response). È destinato esclusivamente all'uso in contesti di red teaming e penetration testing, dove gli operatori sono autorizzati dai proprietari dei sistemi.

### Funzionalità principali

- **Elevazione dei privilegi**: Verifica se l'utente ha i permessi di amministratore e, in caso contrario, richiede l'elevazione dei privilegi.
- **Download e installazione di PsTools**: Scarica e estrae il toolkit PsTools di Sysinternals per utilizzare `PsExec`.
- **Persistenza tramite servizio Windows**: Crea un servizio Windows per mantenere l'accesso persistente.
- **Terminazione di processi EDR**: Identifica e termina processi di difesa comuni associati a software di sicurezza EDR.
- **Download ed esecuzione di un payload malevolo**: Scarica un eseguibile da una fonte esterna ed esegue il file con privilegi elevati utilizzando `PsExec`.

### Prerequisiti

- **Sistema operativo**: Windows.
- **Privilegi di amministratore**: Lo script richiede privilegi di amministratore per eseguire alcune delle sue operazioni, come la creazione di servizi e la terminazione dei processi di sicurezza.
- **Connessione Internet**: Necessaria per scaricare gli strumenti e il payload malevolo.

### Uso

1. **Scaricare e preparare lo script**: Copiare lo script Python su un sistema Windows.
2. **Esecuzione con privilegi elevati**: Lo script verificherà automaticamente se l'utente ha i permessi di amministratore e, se necessario, richiederà l'elevazione.
3. **Download e installazione di PsTools**: Lo script scaricherà e installerà `PsExec` da Sysinternals.
4. **Download del payload malevolo**: Il payload viene scaricato da un URL configurato e salvato nella cartella di sistema.
5. **Creazione di un servizio persistente**: Un servizio di persistenza viene creato e configurato per l'avvio automatico all'avvio del sistema.
6. **Blocco dei processi di difesa**: Vengono identificati e terminati i processi di software EDR per evitare il rilevamento.

### Dettagli dei Processi EDR Bloccati

Lo script cerca di bloccare i seguenti processi associati a software di difesa:

- **MsMpEng.exe** (Microsoft Defender)
- **SentinelAgent.exe** (SentinelOne)
- **CarbonBlack.exe** (Carbon Black)
- **QualysAgent.exe** (Qualys)
- **ElasticAgent.exe** (Elastic Security)
- **CylanceSvc.exe** (Cylance)

### Avvertenza

Venator è uno strumento destinato a scopi di testing in ambienti controllati. È progettato per essere utilizzato esclusivamente da team autorizzati di red teaming e penetration testing. L'utilizzo non autorizzato di questo strumento può essere illegale. Assicurati di avere i permessi appropriati prima di utilizzare Venator su qualsiasi sistema.

### Note

- **PsExec**: Questo script fa uso di PsExec per eseguire operazioni con privilegi elevati. PsExec è un potente strumento di Sysinternals utilizzato per eseguire processi da remoto e localmente con privilegi di amministratore.
- **Persistenza**: Lo script crea un servizio Windows per ottenere persistenza, garantendo che il payload venga eseguito a ogni avvio del sistema.

### Autore

Venator è stato sviluppato per fini educativi e di test in ambito di sicurezza informatica. L'autore non si assume alcuna responsabilità per l'utilizzo improprio del codice

---

# EN - Venator

### Description

Venator is a Python script used to perform persistence actions and bypass defenses on a Windows system. This script downloads and executes a malicious payload, creates a persistence service, and attempts to terminate some known EDR (Endpoint Detection and Response) processes. It is intended solely for use in red teaming and penetration testing contexts, where operators are authorized by system owners.

### Key Features

- **Privilege Escalation**: Checks if the user has administrative privileges, and if not, requests privilege escalation.
- **Download and Install PsTools**: Downloads and extracts the PsTools toolkit from Sysinternals to use `PsExec`.
- **Persistence via Windows Service**: Creates a Windows service to maintain persistent access.
- **Termination of EDR Processes**: Identifies and terminates common defense processes associated with EDR security software.
- **Download and Execute a Malicious Payload**: Downloads an executable from an external source and runs it with elevated privileges using `PsExec`.

### Requirements

- **Operating System**: Windows.
- **Administrative Privileges**: The script requires admin privileges to perform certain operations, such as creating services and killing security processes.
- **Internet Connection**: Necessary to download tools and the malicious payload.

### Usage

1. **Download and prepare the script**: Copy the Python script onto a Windows system.
2. **Run with elevated privileges**: The script will automatically check if the user has admin rights, and if needed, request elevation.
3. **Download and Install PsTools**: The script will download and install `PsExec` from Sysinternals.
4. **Download the malicious payload**: The payload is downloaded from a configured URL and saved to the system folder.
5. **Create a persistent service**: A persistence service is created and configured to start automatically on system boot.
6. **Blocking defense processes**: The script identifies and kills EDR software processes to avoid detection.

### Details of Blocked EDR Processes

The script attempts to block the following processes associated with defense software:

- **MsMpEng.exe** (Microsoft Defender)
- **SentinelAgent.exe** (SentinelOne)
- **CarbonBlack.exe** (Carbon Black)
- **QualysAgent.exe** (Qualys)
- **ElasticAgent.exe** (Elastic Security)
- **CylanceSvc.exe** (Cylance)

### Warning

Venator is a tool designed for testing purposes in controlled environments. It is meant to be used exclusively by authorized red teaming and penetration testing teams. Unauthorized use of this tool may be illegal. Ensure that you have the proper permissions before using Venator on any system.

### Notes

- **PsExec**: This script uses PsExec to run elevated processes. PsExec is a powerful tool from Sysinternals used to execute processes both remotely and locally with administrator privileges.
- **Persistence**: The script creates a Windows service for persistence, ensuring the payload is executed at every system startup.

### Author

Venator was developed for educational and testing purposes in the field of cybersecurity. The author takes no responsibility for improper use of the code.
