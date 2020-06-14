## Configuration Steps for Gitpy (Before Installation : 2 minutes)

Gitpy works on Username & Token of a GitHub Account. So it requires few configuration before Installation.

[Get your Personal Access Token for GitHub Account](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)

For configuration we have two methods available.

## Download gitpy

```
# git clone https://github.com/babygame0ver/gitpy.git && cd gitpy

```

### Method 1. Using Configuration from Local File.

- Create a File with username and token & name it config.json .

![alt text](tests/after_install/media/file_config/1-config_file.PNG)

- Copy the absolute path of config file from file system.

![alt text](tests/after_install/media/file_config/2-config_file_path.png)

- Change the **git_config_path** variable in **gitpy/core/auth.py**

![alt text](tests/after_install/media/file_config/3-config_file_path_in_gitpy.PNG)

---

### Method 2. Creating Environment variable 'username' & 'token' in your machine.

- Obtain Access token from your GitHub Account.

- After obtaining Access token add your Username & Token to Environment variables in your Machine.

### For Windows

1. Username

![alt text](tests/after_install/media/env/1-adding-username.PNG)

2. Token

![alt text](tests/after_install/media/env/2-adding-token.PNG)

### For Linux/MAC

```
export username="yourgithubusername"
export token="yoursecretaccesstoken"
```
