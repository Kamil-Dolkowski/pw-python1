eskadra.bielik.ai

# Azure CLI:
- dla devops'ów
- szybkie wdrażanie
- powtarzalność
- niezawodność
- więcej możliwości, parametrów niż przeglądarka

## Azure CLI:
- sprawdzać wersję 
- aktualizować
- opisać jaka wersja CLI jest użyta
- MFA 

## Instalacja
```
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

az --version
```

## Konto Azure
```bash
cat .azure/azureProfile.json

az account list
az account list --output table

# Zmiana subskrypcji
az account set --subscription mysubscription
```

credentiale - klucze

## Service Principal:
- izolacja dostępu do zasobów

Active Directory

```bash
# Utworzenie service principal
az ad sp create-for-rbac --name "MójServicePrincipal" --role "Contributor" --scopes "/subsiptions/<subscription_id>"

# Zalogowanie na service principal
az login --service-principal -u <login> -p <password> --tenant <id>
```

# Virtual Machine

```bash
az vm list

az group list
```

### 1. Utworzenie Resource group

```bash
az group create --name "CLI-Workshop-RG" --location "westeurope"

az group list --output table
az group show --name "CLI-Workshop-RG"
```

### 2. Usunięcie Resource Group

```bash
az group delete --resource-group rg-storage

az group delete --resource-group CLI-Workshop-RG --yes --no-wait
```

### 3. Storage

```bash
az storage account list

az group create --name "cli-tutorial" --location "polandcentral"

az storage account create \
> --name mojstorage101010 \
> --resource-group cli-tutorial \
> --location "polandcentral" \
> --sku Standard_LRS \
> --kind StorageV2
```

### *Logowanie przez tenant
```bash
az login --tenant <tenant_id>
```

### 3. Storage c.d

```bash
az storage account list
az storage account list --resource-group cli-tutorial

az storage account keys list --resource-group cli-tutorial --account-name mojstorage101010 --output table
```

### 4. Kontener blob

```bash
az storage container create --name mojkontener --account-name mojstorage101010 --public-access blob --auth-mode login
```
*dla typu blob, przez logowanie nie ma możliwości dostępu (public)

### 5. Virtual Machine

```bash
az vm list

az vm create --resource-group cli-tutorial --name myVMPW --image Ubuntu2404 --size Standard_B1s --admin-username azureuser --generate-ssh-keys --no-wait

az vm show -d --resource-group cli-tutorial --name myVMPW --query publicIps
```

```bash
az vm stop --ids /subscriptions/<subscription_id>/resourceGroups/CLI-TUTORIAL/providers/Microsoft.Compute/virtualMachines/myVMPW

az vm start --ids /subscriptions/<subscription_id>/resourceGroups/CLI-TUTORIAL/providers/Microsoft.Compute/virtualMachines/myVMPW

az vm restart --ids /subscriptions/<subscription_id>/resourceGroups/CLI-TUTORIAL/providers/Microsoft.Compute/virtualMachines/myVMPW
```

```bash
az vm list --query "[?resourceGroup=='CLI-TUTORIAL'].{Name:name, Location:location, Size:hardwareProfile.vmsize}" --output table
```

jamespath

```bash
az vm show -d --resource-group cli-tutorial --name myVMPW --query publicIps
# "74.248.115.78"

az vm show -d --resource-group cli-tutorial --name myVMPW --query publicIps --output tsv
# 74.248.115.78

VM_IP=$(az vm show -d --resource-group cli-tutorial --name myVMPW --query publicIps --output tsv)

echo $VM_IP
```

&nbsp;

### Na zakończenie - "wyłączenie" VM'ki

```bash
az group delete --resource-group cli-tutorial
```