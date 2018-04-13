from Component_py.stubs import require, __pragma__  # __:skip
React = require("react")
rn = require("react-native"); \
    Text, View = rn.Text, rn.View

def Header(props):
    text_style, view_style = \
        _s["textStyle"], _s["viewStyle"]
    return __pragma__("js", "{}", """ (
        <View style={view_style}>
            <Text style={text_style}>{props.header_text}</Text>
        </View>
    ); """)

styles = _s = {
    "viewStyle": {
        "backgroundColor": "#F8F8F8",
        "justifyContent": "center",
        "alignItems": "center",
        "height": 80,
        "paddingTop": 25,
        "shadowColor": "#000",
        "shadowOffset": { "width": 0, "height": 2 },
        "shadowOpacity": 0.2,
        "elevation": 2,
        "position": "relative"
    },
    "textStyle": {
        "fontSize": 20
    }
}
