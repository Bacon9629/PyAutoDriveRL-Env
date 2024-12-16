import subprocess


if __name__ == '__main__':
    # path_list = [
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\B10915004@ 鄭典_1043371_assignsubmission_file\B10915004,M11352021\PyAutoDriveRL-Env',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11201105@ 游輝哲_1043365_assignsubmission_file\m11201105\PyAutoDriveRL-Env-main',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\m11215118_m11215119\PyAutoDriveRL-Env',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11215128\PyAutoDriveRL-Env',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352004_M11352008\PyAutoDriveRL-Env-main',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352005@ 林昌明_1043359_assignsubmission_file\m11352005\PyAutoDriveRL-Env',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352006\PyAutoDriveRL-Env',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352007@ 單以仁_1043375_assignsubmission_file\M11352007\PyAutoDriveRL-Env-main',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352004_M11352008_重複繳交\PyAutoDriveRL-Env-main',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352013@ 王冠文_1043360_assignsubmission_file\m11352013\PyAutoDriveRL-Env',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352015@ 黃梓軒_1043363_assignsubmission_file\m11352015\PyAutoDriveRL-Env-origin',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352016@ 謝昕諺_1043349_assignsubmission_file\M11352016_M11352006\PyAutoDriveRL-Env-main',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352017@ 陳威丞_1043357_assignsubmission_file\M11352017\PyAutoDriveRL-Env-main',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352018@ 賴立恩_1043350_assignsubmission_file\M11352018\PyAutoDriveRL-Env',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352020\PyAutoDriveRL-Env',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352026@ 曹濟_1043364_assignsubmission_file\M11352001&M11352026\PyAutoDriveRL-Env',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352031@ 羅子程_1043353_assignsubmission_file\m11352012_m11352031\PyAutoDriveRL-Env',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352034@ 歐銘耘_1043354_assignsubmission_file\m11352034\PyAutoDriveRL-Env',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352035\M11352035',
    #     r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352002_M11352802\PyAutoDriveRL-Env',
    # ]

    path_dict = {
        'B10915004 鄭典、M11352021 徐瑞廷': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\B10915004@ 鄭典_1043371_assignsubmission_file\B10915004,M11352021\PyAutoDriveRL-Env',
        'M11201105 游輝哲': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11201105@ 游輝哲_1043365_assignsubmission_file\m11201105\PyAutoDriveRL-Env-main',
        'M11215118 譚豪朋、M11215119 雲椲荃': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\m11215118_m11215119\PyAutoDriveRL-Env',
        'M11215128 葉威佑': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11215128\PyAutoDriveRL-Env',
        'M11352004 蔡哲旻、M11352008 曾渝軒': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352004_M11352008\PyAutoDriveRL-Env-main',
        'M11352005 林昌明': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352005@ 林昌明_1043359_assignsubmission_file\m11352005\PyAutoDriveRL-Env',
        'M11352006 吳建頤、M11352016 謝昕諺': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352006\PyAutoDriveRL-Env',
        'M11352007 單以仁': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352007@ 單以仁_1043375_assignsubmission_file\M11352007\PyAutoDriveRL-Env-main',
        'M11352013 王冠文、M11352029 黃浚廷': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352013@ 王冠文_1043360_assignsubmission_file\m11352013\PyAutoDriveRL-Env',
        'M11352015 黃梓軒': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352015@ 黃梓軒_1043363_assignsubmission_file\m11352015\PyAutoDriveRL-Env-origin',
        'M11352017 陳威丞': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352017@ 陳威丞_1043357_assignsubmission_file\M11352017\PyAutoDriveRL-Env-main',
        'M11352018 賴立恩': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352018@ 賴立恩_1043350_assignsubmission_file\M11352018\PyAutoDriveRL-Env',
        'M11315022 余承勳、M11352020 余東樺': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352020\PyAutoDriveRL-Env',
        'M11352026 曹濟、M11352001 吳姿伶': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352026@ 曹濟_1043364_assignsubmission_file\M11352001&M11352026\PyAutoDriveRL-Env',
        'M11352012 鄭語萱、M11352031 羅子程': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352031@ 羅子程_1043353_assignsubmission_file\m11352012_m11352031\PyAutoDriveRL-Env',
        'M11352034 歐銘耘': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352034@ 歐銘耘_1043354_assignsubmission_file\m11352034\PyAutoDriveRL-Env',
        'M11352035 吳冠霖': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352035\M11352035',
        'M11352802 Alexandre Morinvil、M11352002 江柏宏': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11352002_M11352802\PyAutoDriveRL-Env',
        'M11352023 徐彥崴': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\m11352023\m11352023\PyAutoDriveRL-Env',

        'M11315002 黃正鵬、M11352030 詹岫尹': r'Z:\MiiSLab_Work\1. 課程相關資料\2024 RL\期末資料夾\大家的package\M11315002黃正鵬Ｍ11352030詹岫尹\PyAutoDriveRL-Env',
    }

    path = path_dict['M11352023 徐彥崴']
    
    # print(path)
    process = subprocess.Popen(['python', 'record_script.py', path])
    process.wait()

# wsl
# source activate autodrive_rl
# cd /mnt/c/Users/miisl/PyAutoDriveRL-Env/M11315002黃正鵬Ｍ11352030詹岫尹/PyAutoDriveRL-Env
# WANDB_MODE=offline python inference_template.py