"""
The projects map spoofing system module.
"""


def setup_database_import_path() -> None:
    from sys import path as module_paths
    from os import system as cmd_input
    import pathlib
    from time import sleep

    project_root_directory = pathlib.Path.cwd()

    module_paths.append(f"{project_root_directory}/main_program/source/coding/database/exceptions")
    module_paths.append(f"{project_root_directory}/main_program/source/coding/database")
    module_paths.append(f"{project_root_directory}/main_program/source/coding")

setup_database_import_path()


from exceptions.unexpected_argument_type import UnexpectedArgumentTypeError
from exceptions.direct_run_error import DirectRunError
from packages import (
    QObject,
    folium,
    json,
)


class MapSpoofer(QObject):
    def __init__(self, latitude: int, longitude: int):
        self.latitude = latitude
        self.longitude = longitude

        self.generated = False

        super(QObject, self).__init__()

    def start(self):
        self.generated = True

        self._map_image_html = folium.Map(
        location=[self.latitude, self.longitude], 
        tiles="Cartodb dark_matter",
        max_bounds=True,
        zoom_start=2, 
        max_zoom=13,
        min_zoom=2, 
        )

        target_icon = folium.CustomIcon(
            icon_image="main_program/source/ui_design/resources/pictures/target_icon.png",
            icon_size=[65, 65]
        )
        
        target_marker = folium.Marker(
            location=[self.latitude, self.longitude],
            tooltip="Exact target location.",
            icon=target_icon
        )

        target_radius_marker = folium.CircleMarker(
            location=[self.latitude, self.longitude],
            tooltip="Target is in this area.",
            radius=44,
            color="red",
            fill_color='red',
        )


        target_marker.add_to(self._map_image_html)
        target_radius_marker.add_to(self._map_image_html)

        return self._map_image_html

    def save_as_html_file(self, file_path: str) -> None:
        self._map_image_html.save(outfile=file_path)

    def save_as_geojson(self, file_path: str) -> None:
        if not self.generated:
            raise PermissionError("No spoof result to save, please finish the spoofing operation before attempting to save.")

        if not isinstance(file_path, str):
            raise UnexpectedArgumentTypeError(inputted_argument=file_path, expected_argument_type=str)
        
        map_image_geojson = json.loads(self._map_image_html.to_json())

        with open(file_path, "w") as geojson_file:
            json.dump(map_image_geojson, geojson_file, indent=4)


module_is_runned_directly = __name__ == "__main__"
if module_is_runned_directly:
    raise DirectRunError(
        "Database modules are not intended to run directly, they are produced for import usage only."
    )