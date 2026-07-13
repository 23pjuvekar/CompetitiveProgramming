class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:

        login_m = int(loginTime[:2]) * 60 + int(loginTime[3:])
        logout_m = int(logoutTime[:2]) * 60 + int(logoutTime[3:])
        
        login_start = ceil(login_m / 15) * 15
        logout_end = floor(logout_m / 15) * 15
        
        if login_m > logout_m:
            return (24 * 60 - login_start + logout_end) // 15
        return max(0, (logout_end - login_start) // 15)
