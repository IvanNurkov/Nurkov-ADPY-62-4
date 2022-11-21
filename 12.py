#https://swapi.dev/api/people/1
# class MyRange:
#
#     def __init__(self, star, end):
#         self.star = star
#         self.end = end
#
#     def __iter__(self):
#         self.cursor = self.star - 1
#         return self
#
#
#     def __next__(self):
#         self.cursor += 1
#         if self.cursor >= self.end:
#             raise StopIteration
#         return self.cursor
#
#
# for item in MyRange(1, 4):
#     print(item)
# import requests as r
#
# class SwPeople:
#
#     def __init__(self):
#         pass
#
#     def __iter__(self):
#         self.nex_page = "https://swapi.dev/api/people/"
#         self.current_batch = []
#
#         return self
#
#     def __next__(self):
#         if not self.nex_page and not self.current_batch:
#             raise StopIteration
#         if not self.current_batch:
#             res = r.get(self.nex_page).json()
#             self.current_batch = res['results']
#             self.nex_page = res['next']
#         return self.current_batch.pop()
#
# for item in SwPeople():
#     print(item)

# def hello_world():
#     while True:
#         yield 'Hi!'
#
# hw = hello_world()
# for item in hw:
#     print(item)

# def get_sw_people():
#     nex_page = 'https://swapi.dev/api/people/'
#     while True:
#         res = r.get(nex_page).json()
#         nex_page = res['next']
#         people = res['results']
#         yield from people
#         # for person in people:
#         #     yield person
#
# for item in get_sw_people():
#     print(item)

# list_of_lists_1 = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f', 'h', False],
#     [1, 2, None]
# ]
# print(list_of_lists_1[0])
# print(len(list_of_lists_1))
# for i in list_of_lists_1:
#     print(i)


list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


ready_list = []
for i in list_of_lists_1:
    for a in i:
        ready_list.append(a)
print(ready_list)
