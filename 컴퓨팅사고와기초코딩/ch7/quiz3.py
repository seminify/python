korean_dict = dict()
korean_dict['하나'] = 'one'
korean_dict['둘'] = 'two'
korean_dict['셋'] = 'three'
korean_dict['넷'] = 'four'
korean_dict['다섯'] = 'five'
korean_dict['여섯'] = 'six'
korean_dict['일곱'] = 'seven'
korean_dict['여덟'] = 'eight'
korean_dict['아홉'] = 'nine'
korean_dict['열'] = 'ten'
while True:
    dict = input('단어를 입력하시오: ')
    if dict != '끝':
        print(korean_dict[dict])
    else:
        break
