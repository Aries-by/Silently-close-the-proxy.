import winreg
import ctypes

def force_disable_proxy():
    """强制关闭Windows代理并刷新，无控制台输出"""
    try:
        # 打开注册表
        internet_settings_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, internet_settings_path, 0, winreg.KEY_WRITE)
        
        # 强制将 ProxyEnable 设为 0
        winreg.SetValueEx(registry_key, "ProxyEnable", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(registry_key)
        
        # 刷新系统网络设置
        INTERNET_OPTION_REFRESH = 37
        INTERNET_OPTION_SETTINGS_CHANGED = 39
        internet_set_option = ctypes.windll.wininet.InternetSetOptionW
        internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
        internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
        
    except Exception:
        # 因为是静默脚本，即使发生错误也不抛出弹窗打扰用户
        pass

if __name__ == "__main__":
    force_disable_proxy()