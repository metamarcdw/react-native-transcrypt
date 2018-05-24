from Component_py.stubs import require, console, __pragma__  # __:skip
from Component_py.component import destruct
from components.Card import Card
from components.CardSection import CardSection
from components.Button import Button

React = require("react")
View, Text, Image, Linking = \
    destruct(require("react-native"), "View", "Text", "Image", "Linking")


def AlbumDetail(props):
    artist, image, thumbnail_image, title, url = \
        destruct(props.album,
                 "artist", "image", "thumbnail_image", "title", "url")
    (header_content_style,
     header_text_style,
     thumbnail_style,
     thumbnail_container_style,
     image_style) = styles.values()

    def on_press(): return Linking.openURL(url)

    return __pragma__("js", "{}", """ (
        <Card>
            <CardSection>
                <View style={thumbnail_container_style}>
                    <Image
                        source={{ "uri": thumbnail_image }}
                        style={thumbnail_style} />
                </View>
                <View style={header_content_style}>
                    <Text style={header_text_style}>
                        {title}
                    </Text>
                    <Text>{artist}</Text>
                </View>
            </CardSection>

            <CardSection>
                <Image
                    source={{ "uri": image }}
                    style={image_style} />
            </CardSection>

            <CardSection>
                <Button onPress={on_press}>
                    Buy Now
                </Button>
            </CardSection>
        </Card>
    ); """)


styles = {
    "headerContentStyle": {
        "flexDirection": "column",
        "justifyContent": "space-around"
    },
    "headerTextStyle": {
        "fontSize": 18
    },
    "thumbnailStyle": {
        "height": 50,
        "width": 50
    },
    "thumbnailContainerStyle": {
        "justifyContent": "center",
        "alignItems": "center",
        "marginLeft": 10,
        "marginRight": 10
    },
    "imageStyle": {
        "height": 300,
        "flex": 1,
        "width": None
    }
}
