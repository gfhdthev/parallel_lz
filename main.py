#gfhdthev
#Лабораторная работа №6
#Основной файл


from first import one_thread, any_therds
from second import multi_processing
from third import async_queue


#Проверка на прямoй запуск
if __name__ == '__main__':
    one_thread()
    any_therds()
    multi_processing()
    async_queue()