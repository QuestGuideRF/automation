import subprocess
from pyfiglet import figlet_format
from termcolor import cprint
logo ='Git-Commands'
class color :
    NOTICE ='\033[91m'
    END ='\033[0m'
info =color .NOTICE ++color .END
dict ={}
def run (*args ):
    return subprocess .check_call (['git']+list (args ))
def clone ():
    print ('\nСначала вас спросят имя пользователя, а затем имя репозитория.\n')
    user =input ('User: ')
    repo =input ('Repository: ')
    subprocess .Popen (['git','clone','https://github.com/'+user +'/'+repo +'.git'])
def commit ():
    commit_message =input ('\nВведите сообщение о фиксации: ')
    run ('commit','-am',commit_message )
    run ('push','-u','origin','master')
def branch ():
    branch =input ('\nВведите название ветки, которую хотите создать: ')
    run ('checkout','-b',branch )
    choice =input ('\nХотите отправить ветку на GitHub прямо сейчас? (да/нет): ').lower ()
    if choice =='y':
        run ('push','-u','origin',branch )
    else :
        print ('\nХорошо, до свидания!\n')
def pull ():
    print ('\nИзвлекает изменения из текущей папки, если инициализирован *.git.')
    choice =input ('\nХотите получить изменения с GitHub? (да/нет): ').lower ()
    if choice =='y':
        run ('pull')
    else :
        print ('\nХорошо, до свидания!\n')
def fetch ():
    print ('\nИзвлекает изменения из текущей папки.')
    run ('fetch')
def merge ():
    branch =input ('\nВведите название вашего филиала: ')
    run ('merge',branch )
def reset ():
    filename =input ('\nВведите имя вашего файла: ')
    run ('reset',filename )
def blame ():
    file =input ('\nВведите имя файла: ')
    run ('blame',file )
def main ():
    cprint (figlet_format (logo ,font ='slant'),'green')
    print (f'{info } \n')
    print ('Используемые команды: клонирование, фиксация, ветвление, извлечение, выборка, слияние, сброс и обвинение.')
    choose_command =input ('Введите команду, которую вы хотите использовать: ').lower ()
    dict ={
    'clone':clone ,
    'commit':commit ,
    'branch':branch ,
    'pull':pull ,
    'fetch':fetch ,
    'merge':merge ,
    'reset':reset ,
    'blame':blame
    }
    dict .get (choose_command ,lambda :"Invalid")()
if __name__ =='__main__':
    main ()