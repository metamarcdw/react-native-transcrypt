from Component_py.stubs import require, console, __pragma__  # __:skip
from Component_py.component import Component
from components.AlbumDetail import AlbumDetail
React = require("react")
ScrollView = require("react-native").ScrollView
fetch = lambda s: None  # __:skip

class AlbumList(Component):
    def __init__(self, props):
        super().__init__(props)
        self.state = { "albums": [] }

    def componentDidMount(self):
        def parse(response): return response.json()
        def resolve(data): self.setState({ "albums": data })
        def reject(error): console.log(error)

        promise = fetch("https://rallycoding.herokuapp.com/api/music_albums")
        promise.then(parse).then(resolve).catch(reject)

    def render(self, props):
        console.log(self.state)

        def render_albums(album):
            return __pragma__("js", "{}", """ (
                <AlbumDetail
                    key={album.title}
                    album={album} />
            ); """)

        return __pragma__("js", "{}", """ (
            <ScrollView>
                { map(render_albums, self.state.albums) }
            </ScrollView>
        ); """)
