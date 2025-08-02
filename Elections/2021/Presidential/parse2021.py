# edit string if it starts with 2-digits and '-'
def editStations(df):
    df.station = df.station.apply(lambda x: x[3:]

                                  # Facing errors with if-else statement.
                                  # if isinstance(x[:2], int) else str(x)
                                 )
    return df

