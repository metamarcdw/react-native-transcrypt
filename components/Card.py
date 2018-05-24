from Component_py.stubs import require, __pragma__  # __:skip
React = require("react")
View = require("react-native").View


def Card(props):
    container_style, = styles.values()
    return __pragma__("js", "{}", """ (
        <View style={container_style}>
            {props.children}
        </View>
    ); """)


styles = {
    "containerStyle": {
        "borderWidth": 1,
        "borderRadius": 2,
        "borderColor": "#DDD",
        "borderBottomWidth": 0,
        "shadowColor": "#000",
        "shadowOffset": {"width": 0, "height": 2},
        "shadowOpacity": 0.1,
        "shadowRadius": 2,
        "elevation": 1,
        "marginLeft": 5,
        "marginRight": 5,
        "marginTop": 10
    }
}
