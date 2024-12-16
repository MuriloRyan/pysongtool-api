
def get_scale_validation(root_note: str, scale_name: str, scales_list: dict) -> dict:
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    root_note = root_note.upper()

    response = {}
    strikes = 0

    if root_note not in notes:
        strikes += 1

        response['is_valid'] = False
        response[f'strike {strikes}'] = {
            'is_valid': False,
            'exception': 'WrongNote',
            'message': f'You entered a wrong note, {root_note} is not a valid note, remmember to use only standard and sharp notes (C,C#,D,#,...)'
        }


    if scale_name not in scales_list:
        strikes += 1

        response['is_valid'] = False
        response[f'strike {strikes}'] = {
            'is_valid': False,
            'exception': 'WrongScale',
            'message': f'You entered an invalid name, {scale_name} is not a valid musical scale name'
        }


    if strikes == 0:
        response['is_valid'] = True
        response['message'] = 'All data has been validated sucessfully'
    
    return response