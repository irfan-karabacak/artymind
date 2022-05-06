class styles:
    text_style = """QLabel{
        min-height: 50px;
        width: 100px;
        color: white;
        background-color: rgba(255, 255, 255, .0);
    }
    """
    text_edit_style = """QTextEdit{
            color: white;
            padding: 5px;
            max-height: 200px;
            max-width: 736px;
            min-width: 736px;
        }
    """
    button_style = """QPushButton{
        min-height: 50px;
        max-width: 200px;
        margin-top: 10px;
        margin-right: 30px;
        border-radius : 100%; 
        border : 2px solid black
        }"""
    text_style_with_right_margin = """QLabel{
        min-height: 50px;
        width: 100px;
        color: white;
        background-color: rgba(255, 255, 255, .0);
    }
    """
    text_style_without_margin = """QLabel{
        width: 100px;
        color: white;  
        background-color: rgba(255, 255, 255, .0);
    }
    """

    combobox_style = """QComboBox{
        height: 40px;
        min-width: 736px;
        max-width: 736px;
        border: 2px solid white;
        border-radius: 5px;
        padding: 5px;
        background: black;
        color: white;
        margin: 0 0 0 0;
        }
        QComboBox QAbstractItemView {
            background-color: black; 
            color: white;
            border-radius: 10px;
        }"""

    slider_style = """QSlider{
        height: 15px;
        min-width: 100px;
        }"""