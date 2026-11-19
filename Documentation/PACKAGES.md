# Packages used in this project

### For Package Installations We Need a 'Virtual Environment'
```bash
python -m venv .venv
```

### For Successful Activation of VM
```bash
./.venv/Scripts/activate
```

### I Ran Into An Error
```
./.venv/Scripts/activate : File C:\Users\Dylan\Desktop\VSCode\FordhamVehicle\.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this 
system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ ./.venv/Scripts/activate
+ ~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

### PowerShell Fix
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---
# Installations

### Pytest for easy unit testing
```bash
pip install pytest
```

- This will install pytest to my virtual envrionment along with any other dependencies for the pytest package

### Freeze to requirements.txt
```bash
pip freeze > requirements.txt
```
