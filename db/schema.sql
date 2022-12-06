DROP TABLE if EXISTS lists;
DROP TABLE if EXISTS parts;

CREATE TABLE lists (
    id integer NOT NULL,
    username text,
    json_list text
);

CREATE TABLE cpus(
    id integer NOT NULL,
    part_name text,
    core_count integer,
    thread_count integer,
    base_clock real,
    boost_clock real,
    hyperthreading integer,
    watts integer,
    price real
)

CREATE TABLE mobos(
    id integer NOT NULL,
    part_name text,
    ram_type text,
    ram_slots integer,
    chipset text,
    socket text,
    form_factor text,
    price real
)

CREATE TABLE ram_kits(
    id integer NOT NULL,
    part_name text,
    capacity integer,
    speed integer,
    cas_latency integer,
    amount_of_sticks integer,
    price real
)

CREATE TABLE gpus(
    id integer NOT NULL,
    part_name text,
    core_count integer,
    base_clock integer,
    boost_block integer,
    mem_clock integer,
    vram integer,
    watts integer,
    price real
)

CREATE TABLE drives(
    id integer NOT NULL,
    part_name text,
    capacity integer,
    interface text,
    price real
)

CREATE TABLE psus(
    id integer NOT NULL,
    part_name text,
    wattage integer,
    modular text,
    efficiency text,
    fanSize integer,
    price real
)

CREATE TABLE coolers(
    id integer NOT NULL,
    part_name text,
    watts integer,
    fans text,
    air_liquid text,
    price real
)

CREATE TABLE cases(
    id integer NOT NULL,
    part_name text,
    included_fans text,
    compatible_fans text,
    psu_type text,
    psu_size text,
    dimensions text,
    glass text,
    price real
)