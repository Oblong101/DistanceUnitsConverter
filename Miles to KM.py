from inquirer import prompt, List, Text

questions = [
    List('method',
        message="Kilometers to Miles (KTM) or Miles to Kilometers (MTK)?",
        choices=['KTM', 'MTK'],
    ),
    Text('distance',
        message="Input the distance",
    )
]

answers = prompt(questions)

match answers['method']:
    case 'KTM':
        convertedDistance = float(answers['distance']) * 1.60934
        print(f"{convertedDistance} kilometers")
        pass
    case 'MTK':
        convertedDistance = float(answers['distance']) / 1.60934
        print(f"{convertedDistance} miles")
        pass
    case _:
        pass
