from phue import Bridge
ip =''
b =Bridge (ip )
b .connect ()
lights =b .get_light_objects ('name')
dict ={}
def movie ():
    for light in lights :
        lights [light ].on =True
        lights [light ].hue =5000
        lights [light ].saturation =100
def turn_off ():
    for light in lights :
        lights [light ].on =False
def main ():
    print ('Используемые команды: фильм и Turn_off.')
    choose_command =input ("Введите команду, которую вы хотите использовать: ").lower ()
    dict ={
    'movie':movie ,
    'turn_off':turn_off ,
    }
    dict .get (choose_command ,lambda :'Invalid')()
if __name__ =='__main__':
    main ()