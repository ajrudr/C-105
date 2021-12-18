import dropbox

class TransferData:
    def __init__(self,access_token):
       self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
        access_token='sl.A-Cf529a6HWKtZ5fG_OgmgsUenikY3Yl8ZEhZvsrAsPU1HM2YljOeZu7AmoqAWrhpluyuDXwwliS1oXa6ONlcR83uUF6kjHrlT38xCdPw6cvSXLfD0KC3c9u2PWjxyImOQaX1N8'
        transferData=TransferData(access_token)

        file_from=input("enterthefilepathtotransfer:")
        file_to=input("enterthefullpathtouploadtodropbox:")

        transferData.upload_file(file_from,file_to)
        print("filehasbeenmoved")

main()