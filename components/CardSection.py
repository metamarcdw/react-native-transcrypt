from Component_py.stubs import require, __pragma__  # __:skip
React = require("react")
View = require("react-native").View


def CardSection(props):
    container_style, = styles.values()
    return __pragma__("js", "{}", """ (
        <View style={container_style}>
            {props.children}
        </View>
    ); """)


styles = {
    "containerStyle": {
        "borderBottomWidth": 1,
        "padding": 5,
        "backgroundColor": "#FFF",
        "justifyContent": "flex-start",
        "flexDirection": "row",
        "borderColor": "#DDD",
        "position": "relative"
    }
}
