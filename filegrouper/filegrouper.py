import os

from filetypes import *
import filetypes

class FileGrouper(object):
    def __init__(self, dir="", prefix_len=5, types=[]):
        self.directory = dir
        self.prefix_len = prefix_len
        self.type_map = {}
        self.outlier_dict = dict() #String (prefix) : list[file if type not in types or group already full]
        #For each prefix; do you already have a group with that prefix
        #Is the file already in the group

        for filetype in types:
            self.type_map[filetype.typename] = filetype.comp_func

        self.groups_ = dict()
        self.walk_directory()


    def walk_directory(self):
        #curr_group = FileGroup(self.type_map.keys())

        #while not curr_group.full:
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                if file.startswith("."):
                    continue
                pref = file[:self.prefix_len]
                if pref not in self.groups_:
                    self.groups_[pref] = FileGroup(self.type_map.keys())
                curr_group = self.groups_[pref]
                curr_group.prefix = pref
                if pref in self.groups_:
                    if self.group_full(curr_group):
                        curr_group.outliers_extra.append(file)
                    if not self.group_full(curr_group):
                        self.add_file(curr_group, os.path.join(root, file))

    def outliers(self):
        return [x for x in self.groups_.values() if x.outliers_extra or not self.group_full(x)]

    def group_full(self, group):
        found_empty = False
        group_vars = vars(group)
        for x in self.type_map.keys():
            if not group_vars[x]:
                found_empty = True
        if found_empty:
            return False
        else:
            group.full = True
        return True

    def add_file(self, group, file):
        for type, func in self.type_map.items():
            if func(file):
                vars(group)[type] = file
                group.empty = False
                self.group_full(group)
                return

    def prefix_in_groups(self, prefix):
        for group in self.groups_:
            if group.prefix == prefix:
                return True
        return False

    def groups(self):
        return self.groups_.items()


class FileGroup(object):
    def __init__(self, file_types=[], prefix=""):
        for x in file_types:
            setattr(self, x, "")

        self.prefix = prefix
        self.full = False
        self.empty = True
        self.outliers_extra = []

    def prefix_match(self, input):
        if input[:len(self.prefix)] == self.prefix:
            return True
        return False
