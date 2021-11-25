import cx_Freeze 
executables = [cx_Freeze.Executable(
    script="jogomarcao2.py", icon = "meujogo/gremio.ico")]

cx_Freeze.setup(
    name= 'O Gremio não vai cair',
    options= {'build_exe': {'packages': ['pygame'],
                            'include_files': ['meujogo']
                            }},
    executables = executables

)