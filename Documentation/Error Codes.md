
# General/Un-categorized

## OblivAeon

* *Common name*: Unknown Error
* *Description*: Any uncaught or unhandled error results in OblivAeon code
* *Source*: Any endpoint can raise this error

# ValueErrors

Usually having to do with bad inputs to the APIs

## Omnitron

* *Common name*: ValueError(Unknown)
* *Description*: Any ValueError not specifically raised by the system will result in Omnitron
* *Source*: Any Lambda

## Ermine

* *Common name*: ValueError(NotHouseRuled)
* *Description*: An Add Game Entry POST fails the Entry Validations (such as duplicate heroes or other ) and is not selected as 'House Ruled' will return this error
* *Source*: Add Game Entry

## Baron Blade

* *Common name*: ValueError(UnparsableQuery)
* *Description*: An attempt to retrieve Statistics had a path that was not parsable
* *Source*: Statistics
