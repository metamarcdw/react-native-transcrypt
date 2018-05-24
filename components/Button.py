from Component_py.stubs import require, __pragma__  # __:skip
from Component_py.component import destruct
React = require("react")
Text, TouchableOpacity = \
    destruct(require("react-native"), "Text", "TouchableOpacity")


def Button(props):
    button_style, text_style = styles.values()
    return __pragma__("js", "{}", """ (
        <TouchableOpacity
            style={button_style}
            onPress={props.onPress}>
            <Text style={text_style}>
                {props.children}
            </Text>
        </TouchableOpacity>
    ); """)


styles = {
    "buttonStyle": {
        "flex": 1,
        "alignSelf": "stretch",
        "backgroundColor": "#FFF",
        "borderRadius": 5,
        "borderWidth": 1,
        "borderColor": "#007AFF",
        "marginLeft": 5,
        "marginRight": 5
    },
    "textStyle": {
        "alignSelf": "center",
        "color": "#007AFF",
        "fontSize": 16,
        "fontWeight": "600",
        "paddingTop": 10,
        "paddingBottom": 10
    }
}
