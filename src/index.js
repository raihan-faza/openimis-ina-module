import messages_ina from "./translations/ina.json";
import flatten from "flat";

const DEFAULT_CONFIG = {
	translations: [{ key: "ina", messages: flatten(messages_ina) }],
};

export const LanguageInaModule = (cfg) => {
	return { ...DEFAULT_CONFIG, ...cfg };
};
