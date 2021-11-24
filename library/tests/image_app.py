from greppo import app

app.base_layer(
    name="CartoDB Light",
    visible=True,
    url="https://cartodb-basemaps-a.global.ssl.fastly.net/light_all/{z}/{x}/{y}@2x.png",
    subdomains=None,
    attribution='&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
)

app.image_layer(
    file_path="tests/data/San_Francisco_Peninsula_by_Sentinel-2_2019-03-11.jpg",
    title="SFO Arial",
    description="SFO Arial Map",
    visible=True,
)
