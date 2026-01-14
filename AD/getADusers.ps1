
[string]$yesOrNo = Read-Host "Do you know the users username?"

if ($yesOrNo == "yes".toLowerCase) {
    [string]$universalValue = Read-Host "What is the users username?"
    Get-ADUser -Identity $universalValue
} else {
    [string]$fullName = Read-Host "What is the users first name and last name"
    Get-ADUser -Filter "displayName -eq $fullName"
}
