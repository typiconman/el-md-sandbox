# List of Identifiers

## Hymnographical Identifies

* `hid` is a unique hymn identifier, e.g., `{{hid=1}} ~Σοῦ ἡ τροπαιοῦχος δεξιά...`.
* `*` is used if the hymn occurs only as an icipit, e.g., `{{hid=1*}} ~Σοῦ ἡ τροπαιοῦχος δεξιά`.

## Liturgical Identifiers

* `lid` is a liturgical identifier
* These are hierarchical, with `/` occuring as a separator character.

### Top Level

These are usually the names of the services.

* `v` - Vespers
* `m` - Matins

More may likely appear.

### Identifiers of Elements Within the Service (liturgical)

* `lihc` - stichera at "Lord, I have cried." There may be 1 block of stichera, in which case all are marked with a sequential number. If there are multiple blocks, the block number is placed first, followed by the number of the sticheron within it (`v/lihc/1/1`, etc.). Stichera for "Glory" and "Now and ever" are marked outside the blocks: `v/lihc/dox` ("glory"), `v/lihc/th` ("theotokion"), and `v/lihc/sth` ("staurotheotokion").
* `pr` - prokeimenon.
* `parem` - Old Testament lessons, for which a sequential number is indicated: `v/parem/1`.
* `lit` - stichera at the lite (for detailed marking see `lihc`).
* `apos` - stichera aposticha (for detailed marking see `lihc`).
* `tr` - troparia, for which a sequential number is also indicated (if there are multiple troparia) and glory/now and ever.

### Matins

* `cath` - cathisma (sessional) hymn, the block number, and the hymn number or glory/now and ever: `u/cath/1/dox`.
* `anab` - Hymns of Ascents (anabathmoi), the block number is indicated first, then the number of the individual hymn or "glory/now and ever."
* `50ps` - sticheron for Psalm 50.
* `can` - canon. For each canon, its sequential number is indicated, within it the odes are marked, and within the ode - the heirmos and troparia. If the text explicitly states "Glory" or theotokion, then instead of the troparion number - `dox` or `th`. Thus, the structure of the first ode of the first canon may look like this:
  * `u/can/1/1/h`
  * `u/can/1/1/1`
  * `u/can/1/1/dox`
  * `u/can/1/1/th`
Additionally, within the canon, the following elements are highlighted:
  * `cath` - the canon number, ode number, cathisma hymn number, or glory/now and ever is indicated: `u/can/1/3/cath/1` (`u/can/1/3/cath/dox`, `u/can/1/3/cath/th`, `u/can/1/3/cath/sth`). 
// NB: However, it is not entirely correct to tie the sessional hymn to a specific canon. But how to avoid this?
  * `kont` - kontakion, the preceding structure is preserved: `u/can/1/6/kont`.
  * `ikos` - oikos, just like the kontakion.
  * `syn` - synaxarion, just in case we indicate that it is for the 6th song: `u/can/1/6/syn`
    * `stih` - stichoi of the synaxarion: `u/can/1/6/syn/stih`
  * `ex` - light/exapostilarion, it can also have a sequential number or glory/now and ever.
* `ainoi` - stichera at the praises (ainoi), for detailed marking see `lihc`
* `apos` - stichera aposticha, for detailed marking see `lihc`

## Multiple IDs

IDs are separated with spaces, e.g., `{{hid=1 lid=m/can/1/1/h tone=1}} ~Σοῦ ἡ τροπαιοῦχος δεξιά`.

Other categories may be indicated:

* `tone` - the tone (mode); the Slavic system is used (1 through 8)
* `prosom` - the `hid` of the automelon for a prosomeon

The `tone` property should be inherited, e.g., we specify `tone` for the hirmos of the first ode of the canon and for all subsequent elements it is assumed.
