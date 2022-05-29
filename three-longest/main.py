# https://stackoverflow.com/questions/72425497/how-to-find-the-highest-length-of-elements-in-a-list-of-list-in-python

if __name__ == "__main__":
    all_list = [
        ['orange', 'the dress', '5643,43245,5434,22344,34533'],
        ['pink', 'cars', '12322,4455,533,2344,24324,64466,543342'],
        ['dark pink' 'doll', '12422,4533,6446,35563'],
        ['blue', 'car', '43356,53352,546'],
        ['sky blue', 'dress', '63463,3635432,354644,6544,6444,644,74245'],
    ]
    print(sorted(all_list, key=lambda l: len(l[-1].split(',')), reverse=True)[:3])
