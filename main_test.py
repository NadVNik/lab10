from main import get_pass_list

def test_pass_list_all():
    data = ['0,1,2,3,4,male', '0,1,2,3,4,female', '0,1,2,3,4,female']
    assert get_pass_list(data, '1', 'мужчины') == data

def test_pass_list_save():
    data = ['0,1,2,3,4,male', '0,1,2,3,4,female', '0,1,2,3,4,female']
    assert get_pass_list(data, '1', 'мужчины') == ['0,1,2,3,4,male']




