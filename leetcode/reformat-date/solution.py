class Solution:
    def reformatDate(self, date: str) -> str:

        arr = date.split(" ")
        months = {
            "Jan":"01",
            "Feb":"02",
            "Mar":"03",
            "Apr":"04",
            "May":"05",
            "Jun":"06",
            "Jul":"07",
            "Aug":"08",
            "Sep":"09",
            "Oct":"10",
            "Nov":"11",
            "Dec":"12"
        }
        if len(arr[0]) == 3:
            return arr[2] + "-" + months[arr[1]] + "-" + "0" + arr[0][:len(arr[0]) - 2]
        return arr[2] + "-" + months[arr[1]] + "-" + arr[0][:len(arr[0]) - 2]
