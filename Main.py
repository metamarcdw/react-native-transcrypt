from Component_py.stubs import require, __pragma__, module  # __:skip
from components.Header import Header
from components.AlbumList import AlbumList
React = require("react")
View = require("react-native").View

def App():
    return __pragma__("js", "{}", """ (
        <View style={{ "flex": 1 }}>
            <Header header_text={"Albums"} />
            <AlbumList />
        </View>
    ); """)

module.exports = App
