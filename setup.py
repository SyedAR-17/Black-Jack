import cx_Freeze
import pygame
from http.server import executable
executables = [cx_Freeze.Executable("Test.py")]
cx_Freeze.setup(
    name="Black jack",
    options={"bulid_exe": {"packages":["pygame"],"include_files":[r"123.jpg",r"12.jpg","KS.jpg","KD.jpg","KH.jpg","KC.jpg","QS.jpg","QD.jpg","QH.jpg","QS.jpg",
                                                                "AcardH.jpg","AcardC.jpg","AcardD.jpg","AcardS.jpg","JS.jpg","JD.jpg","JH.jpg","JC.jpg"
                                                                 ,"S2.jpg","S3.jpg","S4.jpg","S5.jpg","S6.jpg","S7.jpg","S8.jpg","S9.jpg","S10.jpg","H1.jpg",
                                                                 "H2.jpg","H3.jpg","H4.jpg","H5.jpg","H6.jpg","H7.jpg","H8.jpg","H9.jpg","H10.jpg",
                                                                 "D2.jpg","D3.jpg","D4.jpg",'D5.jpg',"D6.jpg","D7,jpg","D8.jpg","D9.jpg","D10.jpg"
                                                                 "C2.jpg","C3.jpg","C4.jpg","C5.jpg","C6.jpg","C7.jpg","C8.jpg","C9.jpg","C10.jpg"]}}
    
    
    , executables=executables )
