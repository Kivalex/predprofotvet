with open('monster_game.csv') as f:
    sp =[i.split(',') for i in f.readlines()]
    opportunity = [sp[i][1] for i in range(1, len(sp))]
    health = [sp[i][-2] for i in range(1, len(sp))]
    probability = [sp[i][2] for i in range(1, len(sp))]
    regen = []
    '''Описание аргуменнтов
    opportunity = значение возможности монстра
    health = значение здоровья монстра
    probability = значение вероятности возможности монстра
    regen = значение регенерации монстра
    '''
    for i in range(len(opportunity)):
        if opportunity[i] == 'СЂРµРіРµРЅРµСЂР°С†РёСЏ':
            regen.append(int(health[i]) * int(probability[i]))
    print(f'Регенерация: {max(regen)}')
