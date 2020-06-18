from nornir import InitNornir


def main():
    nr = InitNornir(config_file='config.yaml', logging={'enabled': False})
    nr = nr.filter(name='bostonrtr1')
    bostonrtr1 = nr.inventory.hosts['bostonrtr1']
    print(bostonrtr1)


if __name__ == '__main__':
    main()

