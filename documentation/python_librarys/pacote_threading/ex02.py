import faker, threading, time
fk = faker.Faker('pt_BR')

def Say_Hello(name):
    time.sleep(4)
    print(f'Helooooo, {name}')


def Say_Goodbye(name):
    time.sleep(8)
    print(f'Goodbye, {name}')

hello = threading.Thread(target=Say_Hello, args=(fk.name(),))
gbye = threading.Thread(target=Say_Goodbye, args=(fk.name(),))
gbye.start()
hello.start()
for count in range(20):
    print(count)
    time.sleep(1)