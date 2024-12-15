import subprocess


if __name__ == '__main__':
    path_list = [
        r'E:\share2\B10915004@ 鄭典_1043371_assignsubmission_file\B10915004,M11352021\PyAutoDriveRL-Env',
        r'E:\share2\M11201105@ 游輝哲_1043365_assignsubmission_file\m11201105\PyAutoDriveRL-Env-main',
        r'E:\share2\m11215118_m11215119\PyAutoDriveRL-Env',
        r'E:\share2\M11215128\PyAutoDriveRL-Env',
        r'E:\share2\M11352004_M11352008\PyAutoDriveRL-Env-main',
        r'E:\share2\M11352005@ 林昌明_1043359_assignsubmission_file\m11352005\PyAutoDriveRL-Env',
        r'E:\share2\M11352006\PyAutoDriveRL-Env',
        r'E:\share2\M11352007@ 單以仁_1043375_assignsubmission_file\M11352007\PyAutoDriveRL-Env-main',
        r'E:\share2\M11352004_M11352008_重複繳交\PyAutoDriveRL-Env-main',
        r'E:\share2\M11352013@ 王冠文_1043360_assignsubmission_file\m11352013\PyAutoDriveRL-Env',
        r'E:\share2\M11352015@ 黃梓軒_1043363_assignsubmission_file\m11352015\PyAutoDriveRL-Env-origin',
        r'E:\share2\M11352016@ 謝昕諺_1043349_assignsubmission_file\M11352016_M11352006\PyAutoDriveRL-Env-main',
        r'E:\share2\M11352017@ 陳威丞_1043357_assignsubmission_file\M11352017\PyAutoDriveRL-Env-main',
        r'E:\share2\M11352018@ 賴立恩_1043350_assignsubmission_file\M11352018\PyAutoDriveRL-Env',
        r'E:\share2\M11352020\PyAutoDriveRL-Env',
        r'E:\share2\M11352026@ 曹濟_1043364_assignsubmission_file\M11352001&M11352026\PyAutoDriveRL-Env',
        r'E:\share2\M11352031@ 羅子程_1043353_assignsubmission_file\m11352012_m11352031\PyAutoDriveRL-Env',
        r'E:\share2\M11352034@ 歐銘耘_1043354_assignsubmission_file\m11352034\PyAutoDriveRL-Env',
        r'E:\share2\M11352035\M11352035',
        r'E:\share2\M11352002_M11352802\PyAutoDriveRL-Env',
    ]

    for i in range(2, 3):
        for path in path_list:
            process = subprocess.Popen(['python', 'record_script.py', path, str(i)])
            process.wait()
