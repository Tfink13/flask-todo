DROP TABLE IF EXISTS items;

CREATE TABLE new_tasks (
  id bigserial PRIMARY KEY,
  text text NOT NULL,
  created_at timestamp NOT NULL,
  completed boolean NOT NULL
);
