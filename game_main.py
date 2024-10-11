# thinger for url
# ?vscode-coi=

# imports
import game_util_error as error_handler
import game_util_gameinfo as gameinfo

while True:
    proceed = True

    try:
        numerator = int(input('numerator: '))
        denominator = int(input('denominator: '))
    except:
        error_handler.passError('Numerator or Denominator are not integer or float values', __name__)
        proceed = False
    
    if proceed:
        try:
            result = numerator / denominator
            print(result)
        except:
            zero_division = denominator == 0
            
            not_int = type(numerator) != int or type(denominator) != int
            not_float = type(numerator) != float or type(denominator) != float

            if zero_division:
                error_handler.passError('Division with zero Malfunction', __name__)
            else:
                error_handler.passError('Unknown Exception with division', __name__)
            