
from covid import Covid
from userbot import CMD_HELP
from userbot.events import register


# @borg.on(admin_cmd(pattern="coronavirus (.*)"))
# async def _(event):
@register(outgoing=True, pattern="^.covid (.*)")
async def corona(event):
    await event.edit("`Processing...`")
    country = event.pattern_match.group(1)
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
        output_text = (
            f"`Confirmed   : {country_data['confirmed']}`\n" +
            f"`Active      : {country_data['active']}`\n" +
            f"`Deaths      : {country_data['deaths']}`\n" +
            f"`Recovered   : {country_data['recovered']}`\n\n" +
            f"`New Cases   : {country_data['new_cases']}`\n" +
            f"`New Deaths  : {country_data['new_deaths']}`\n" +
            f"`Critical    : {country_data['critical']}`\n" +
            f"`Total Tests : {country_data['total_tests']}`\n\n" +
            f"Data provided by [Worldometer](https://www.worldometers.info/coronavirus/country/{country})")
        await event.edit(f"Corona Virus Info in {country}:\n\n{output_text}")
    except ValueError:
        await event.edit(
            f"No information found for: {country}!\nCheck your spelling and try again."
        )


def get_country_data(country, world):
    for country_data in world:
        if country_data["country"].lower() == country.lower():
            return country_data
    return {"Status": "No information yet about this country!"}


CMD_HELP.update({
    "covid":
    ".covid <country> \
    \nUsage: CoronaVirus LookUp for specified country if available."
})
