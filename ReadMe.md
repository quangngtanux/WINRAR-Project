# WINAR – oTree Applications

This repository contains the oTree applications developed for the **WINAR** research project, coordinated by *Rustam Romaniuc*.

---

## Requirements

* **Python** 3.11
* **oTree** 5.11.4

The full list of dependencies is provided in [`conda_env.yml`](./conda_env.yml).

---

## Installation


Create the conda environment:

```bash
conda env create -f conda_env.yml
```

Activate the environment:

```bash
conda activate otree5
```

Check that oTree is installed correctly:

```bash
otree --version
```

Expected output:

```
5.11.4
```

---

## Usage

To start the development server:

```bash
otree devserver
```

By default, oTree will run at [http://localhost:8000](http://localhost:8000).

---

## Contact

For any questions regarding these applications, please contact:
**Dimitri Dubois** – [dimitri.dubois@umontpellier.fr](mailto:dimitri.dubois@umontpellier.fr)

