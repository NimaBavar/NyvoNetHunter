"""
The projects map spoofing system module.
"""


def setup_database_import_path() -> None:
    from sys import path as module_paths
    import pathlib

    project_root_directory = pathlib.Path.cwd()

    module_paths.append(f"{project_root_directory}/main_program/source/coding/database/exceptions")
    module_paths.append(f"{project_root_directory}/main_program/source/coding/database")
    module_paths.append(f"{project_root_directory}/main_program/source/coding")

setup_database_import_path()


from packages import (
    pyqtSignal,
    QObject,
    folium,
    json,
    io,
)
from exceptions.direct_run_error import DirectRunError


class MapSpoofer(QObject):
    location_spoofed = pyqtSignal()
    saved_as_html = pyqtSignal()

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
            color="white",
            fill_color='white',
        )


        target_marker.add_to(self._map_image_html)
        target_radius_marker.add_to(self._map_image_html)

        self.location_spoofed.emit()
        return self._map_image_html

    def save_as_html_file(self, file_path: str) -> None:
        self.saved_as_html.emit()
        self._map_image_html.save(outfile=file_path)

    def save_as_geojson(self, file_path: str) -> None:
        if not self.generated:
            raise PermissionError("No spoof result to save, please finish the spoofing operation before attempting to save.")

        if not isinstance(file_path, str):
            argument_type = type(file_path).__name__
            raise ValueError(f"Expected argument type passed for the parameter: ( file_path ): ( str ) | Not: {argument_type}")
        
        map_image_geojson = json.loads(self._map_image_html.to_json())

        with open(file_path, "w") as geojson_file:
            json.dump(map_image_geojson, geojson_file, indent=4)

    def save_as_bytes(self):
        if not self.generated:
            raise PermissionError("No spoof result to save, please finish the spoofing operation before attempting to save.")

        byte_data = io.BytesIO()
        self._map_image_html.save(byte_data, close_file=False)
        self.map_image_bytes = byte_data

        return self.map_image_bytes
    
    def set_latitude(self, latitude) -> None:
        self.latitude = latitude

    def set_longitude(self, longitude) -> None:
        self.longitude = longitude


module_is_runned_directly = __name__ == "__main__"
if module_is_runned_directly:
    raise DirectRunError(
        "Database modules are not intended to run directly, they are produced for import usage only."
    )
