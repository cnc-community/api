# Copyright C&C Community © 2020 by Grant Bartlett
# GPL-2.0 License
# Version: 1.0.0
# Email: support@cnc.community
# Website: https://cnc.community

import obspython as obs
import urllib.request
import urllib.error
import json

url = ""
interval = 900

# Private key names for sources
data_settings_key_rank_name = "rank_source_key"
data_settings_key_wins_name = "wins_source_key"
data_settings_key_losses_name = "losses_source_key"
data_settings_key_points_name = "points_source_key"


# Fetch player profile from API
def fetch_profile():
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            text_response = data.decode('utf-8')
            json_response = json.loads(text_response)
            update_profile(json_response)

    except urllib.error.URLError as err:
        obs.script_log(obs.LOG_WARNING,
                       "Error opening URL '" + url + "': " + err.reason)
        obs.remove_current_callback()


# Update text sources from API response
def update_profile(json_response):

    # Update Rank
    update_text_source(source_rank_name, "Rank #" + str(json_response['rank']))

    # Update Wins
    update_text_source(source_rank_wins_name, "Wins: " +
                       str(json_response['wins']))
    # Update Losses
    update_text_source(source_rank_losses_name, "Lost: " +
                       str(json_response['losses']))
    # Update Points
    update_text_source(source_rank_points_name, "Points: " +
                       str(round(json_response['points'])))


# Update each supplied text source value
def update_text_source(source, data):
    src = obs.obs_get_source_by_name(source)
    src_settings = obs.obs_data_create()
    obs.obs_data_set_string(src_settings, "text", data)
    obs.obs_source_update(src, src_settings)
    obs.obs_data_release(src_settings)

    if src is not None:
        obs.obs_source_release(src)


# OBS Properties and window descriptions
def refresh_pressed(props, prop):
    fetch_profile()


def script_description():
    return "Display your Leaderboard rank from https://cnc.community"


def script_update(settings):
    global url
    global interval
    global source_rank_name
    global source_rank_wins_name
    global source_rank_losses_name
    global source_rank_points_name

    url = obs.obs_data_get_string(settings, "url")
    interval = obs.obs_data_get_int(settings, "interval")

    # Sources for each profile property
    source_rank_name = obs.obs_data_get_string(
        settings, data_settings_key_rank_name)

    source_rank_wins_name = obs.obs_data_get_string(
        settings, data_settings_key_wins_name)

    source_rank_losses_name = obs.obs_data_get_string(
        settings, data_settings_key_losses_name)

    source_rank_points_name = obs.obs_data_get_string(
        settings, data_settings_key_points_name)

    obs.timer_remove(fetch_profile)

    # Also ensure we're not fetching anything less than 15 minutes
    if url != "" and source_rank_name != "" and interval >= 1800:
        obs.timer_add(fetch_profile, interval * 1000)


def script_defaults(settings):
    obs.obs_data_set_default_int(settings, "interval", interval)


# OBS Properties
def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_text(props, "url", "URL", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_int(
        props, "interval", "Update Interval (seconds)", 5, 3600, 1)

    rank_property = obs.obs_properties_add_list(
        props, data_settings_key_rank_name, "Rank Source", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)

    wins_property = obs.obs_properties_add_list(
        props, data_settings_key_wins_name, "Wins Source", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)

    lost_property = obs.obs_properties_add_list(
        props, data_settings_key_losses_name, "Lost Source", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)

    points_property = obs.obs_properties_add_list(
        props, data_settings_key_points_name, "Points Source", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)

    sources = obs.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = obs.obs_source_get_unversioned_id(source)

            if source_id == "text_gdiplus" or source_id == "text_ft2_source":
                name = obs.obs_source_get_name(source)
                obs.obs_property_list_add_string(rank_property, name, name)
                obs.obs_property_list_add_string(wins_property, name, name)
                obs.obs_property_list_add_string(lost_property, name, name)
                obs.obs_property_list_add_string(points_property, name, name)

        obs.source_list_release(sources)

    obs.obs_properties_add_button(props, "button", "Refresh", refresh_pressed)
    return props
