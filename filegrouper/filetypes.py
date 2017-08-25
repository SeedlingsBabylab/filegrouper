class FileType(object):
    def __init__(self, typename, comp_func):
        self.typename = typename
        self.comp_func = comp_func

def audio_bl_comp_func(input):
    if input.endswith(".csv"):
        if "audio" in input:
            return True
    return False

def video_bl_comp_func(input):
    if input.endswith(".csv"):
        if "video" in input:
            return True
    return False

def lena5min_comp_func(input):
    return input_endswith(input, "lena5min.csv")

def silences_comp_func(input):
    return input_endswith(input, "silences.txt")

def video_comp_func(input):
    return input_endswith(input, ".mp4")

def audio_comp_func(input):
    if input.endswith(".wav"):
        if "scrubbed" not in input:
            return True
    return False

def audio_scrubbed_comp_func(input):
    if input.endswith(".wav"):
        if "scrubbed" in input:
            return True
    return False

def opf_not_final_comp_func(input):
    if input.endswith(".opf"):
        if "consensus_final" not in input:
            return True
    return False

def opf_final_comp_func(input):
    if input.endswith(".opf"):
        if "consensus_final" in input:
            return True
    return False

def clan_silences_comp_func(input):
    if input.endswith(".cha"):
        if "silences" in input:
            return True
    return False

def clan_final_comp_func(input):
    if input.endswith(".cha"):
        if "_final" in input and "_merged" not in input:
            return True
    return False

def clan_merged_comp_func(input):
    if input.endswith(".cha"):
        if "newclan_merged" in input and "final" not in input:
            return True
    return False

def clan_merged_final_comp_func(input):
    if input.endswith(".cha"):
        if "newclan_merged" in input and "final" in input:
            return True
    return False

def video_personal_info_comp_func(input):
    return input_endswith(input, "personal_info.csv")

def video_recode_csv_comp_func(input):
    return input_endswith(input, "recode_processed.csv")

def video_recode_csv_orig_comp_func(input):
    return input_endswith(input, "recode_orig_processed.csv")

def audio_recode_csv_orig_comp_func(input):
    return input_endswith(input, "blank_rel_10_orig.csv")

def audio_recode_blank_cha_comp_func(input):
    return input_endswith(input, "blank_rel_10.cha")

def audio_recode_orig_cha_comp_func(input):
    return input_endswith(input, "blank_rel_10_orig.cha")

def clan_sparse_code_comp_func(input):
    return input_endswith(input, "sparse_code.cha")

def lena_cha_comp_func(input):
    return input_endswith(input, ".lena.cha")



def input_endswith(input, suffix):
    if input.endswith(suffix):
        return True
    return False



opf_not_final = FileType("opf_not_final", opf_not_final_comp_func)
opf_final = FileType("opf_final",opf_final_comp_func)
audio_scrubbed = FileType("audio_scrubbed", audio_scrubbed_comp_func)
audio = FileType("audio", audio_comp_func)
video_file = FileType("video", video_comp_func)
audio_bl = FileType("audio_bl", audio_bl_comp_func)
video_bl = FileType("video_bl", video_bl_comp_func)
silences = FileType("silences", silences_comp_func)
lena5min = FileType("lena5min", lena5min_comp_func)
lena_cha = FileType("lena_cha", lena_cha_comp_func)
clan_silences = FileType("clan_silences", clan_silences_comp_func)
clan_final = FileType("clan_final", clan_final_comp_func)
newclan_merged = FileType("newclan_merged", clan_merged_comp_func)
newclan_merged_final = FileType("newclan_merged_final", clan_merged_final_comp_func)
video_personal_info = FileType("video_personal_info", video_personal_info_comp_func)
video_recode_csv = FileType("video_recode_csv", video_recode_csv_comp_func)
video_orig_recode_csv = FileType("orig_video_recode_csv", video_recode_csv_orig_comp_func)
audio_orig_recode_csv = FileType("orig_audio_recode_csv", audio_recode_csv_orig_comp_func)
audio_blank_recode_cha = FileType("audio_recode_cha", audio_recode_blank_cha_comp_func)
audio_orig_recode_cha = FileType("audio_orig_recode_cha", audio_recode_orig_cha_comp_func)
clan_sparsecode = FileType("clan_sparsecode", clan_sparse_code_comp_func)
