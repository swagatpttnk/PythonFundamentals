import json
import shutil


class FileUtil:

    def basic_read_file(self, filepath, filename):
        file = open(filepath + '/' + filename, 'r')
        file_content = file.read()
        file.close()
        print(file_content)

    def basic_write_file(self, filepath, filename):
        username = input('Enter your name:')
        file = open(filepath + '/' + filename, 'w')
        file.write(username)
        file.close()
        print('----reading the written file as follows:-----')
        self.basic_read_file(filepath, filename)

    def findNearByPeopleWhoAreFriend(self):
        friends = input('Enter Friends Name separated by comma, no space please:').split(',')
        people = open('people.txt', 'r')
        people_nearby = [line.strip() for line in people.readline()]
        people.close()

        friend_set = set(friends)
        people_nearby_set = set(people_nearby)
        friend_nearby_set = friend_set.intersection(people_nearby_set)
        nearby_friends_file = open('nearby_friends.txt', 'w')

        for friend in friend_nearby_set:
            print(f'{friend} is nearby Meetup with them')
            nearby_friends_file.write(f'{friend} is nearby Meetup with them')
        nearby_friends_file.close()

    def copy_file(self, srcfilename, destfilename):
        shutil.copy(srcfilename, destfilename)

        # Read the contents of the copied file
        with open(destfilename, 'r') as file:
            contents = file.read()
            print(contents)

    def json_read_file(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def json_write_file(self, records, filename):
        with open(filename, 'w') as file:
            json.dump(records, file)


if __name__ == "__main__":
    demo = FileUtil()
    # demo.basic_read_file('.', 'abc.txt')
    # demo.basic_write_file('.', 'abc.txt')
    # demo.copy_file('sample.txt','output.txt')
    # demo.findNearByPeopleWhoAreFriend()
    records = [{"name": "Swagat", "age": 42}, {"name": "Krish", "age": 52}, {"name": "Rakuten", "age": 23}]
    demo.json_write_file(records, "json_dump.txt")
    jsonrecords = demo.json_read_file("json_dump.txt")

    for index, record in enumerate(jsonrecords):
        print(f'{index}. Name:{record['name']} , Age:{record['age']}')
