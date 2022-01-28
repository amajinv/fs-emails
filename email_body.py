def body_tipo_prd(total_prd, mayor_90):
    email_content = f"""
                        <html>
                            <head>
                                <body>
                                    <p> Estimados Oscar y Luis: </p>
                                    <p> Por favor encuentren a continuación el análisis de F3 tipo producto en estado enviado para locales y cd, con su respectiva antigüedad.</p>
                                    <p> -	Se evidencia un total de ${total_prd} M abiertos del 2021 de los cuales ${mayor_90} M tienen antigüedad mayor a 90 días</p>
                                    <img src="cid:image1">
                                    <p> El detalle de la información se encuentra adjunto.  </p>
                                    <p> Quedo atento en caso de que surja alguna duda con la información anterior.</p>
                                    <p> Saludos cordiales,</p>
                                </body>
                            </head>
                        """
    return email_content