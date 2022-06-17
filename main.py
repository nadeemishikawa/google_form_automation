import urllib
import  random
def generate_url(url):
    group_name = urllib.parse.quote("セッシー")
    student_number = urllib.parse.quote("C0B20000")
    student_name = urllib.parse.quote("山田太郎")
    place_name = urllib.parse.quote("バイト")


    # 36度1分〜7分になる
    morining_temp = 36 + random.randint(1, 7) / 10
    night_temp = 36 + random.randint(1, 7) / 10

    parameter = "?usp=pp_url&entry.987697424={}&entry.1451746778={}&entry.15528679={}&entry.559706162={}&entry.1257304114={}&entry.793511166={}&entry".format(
        group_name,
        student_number,
        student_name,
        morining_temp,
        night_temp,
        place_name
      )
    new_url = f'{url}?usp=pp_url&entry.987697424={group_name}&entry.1451746778={student_number}&entry.15528679={student_name}&entry.559706162={morining_temp}&entry.60078259={night_temp}&entry.793511166={place_name}&entry'
        # "https://docs.google.com/forms/d/e/1FAIpQLSc0QOFKz0DnOO9Wx9LPX3rs3mNghKRIftLC6SNgalsTJyAF7g/viewform{}".format(parameter)
    return new_url

url = 'https://docs.google.com/forms/d/e/1FAIpQLSdELat41CE3MvmKScNKONyMSTMtRmGyQQJnOvZ49Y0ApIJ_yQ/viewform'
new_page = generate_url(url)
print(new_page)
