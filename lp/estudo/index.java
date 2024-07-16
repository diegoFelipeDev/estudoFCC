import java.util.ArrayList;
import java.util.List;
    public class Main {
        public static void main(String[] args) {
        List<String> nomes = new ArrayList<>();
        nomes.add("João");
        nomes.add("Maria");
        nomes.add("Pedro");
        // Loop foreach para percorrer a lista de nomes
        for (String nome : nomes) {
         System.out.println(nome);
        }
    }
}



CREATE TABLE Item (
    ItemID int,
    Name varchar(255),
    Price float,
);



import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .authorizeRequests()
            .antMatchers("/").permitAll() // Permitir acesso à página inicial sem autenticação
            .anyRequest().authenticated() // Todas as outras URLs requerem autenticação
            .and()
            .formLogin()
            .loginPage("/login") // Configurar a página de login personalizada
            .defaultSuccessUrl("/welcome") // Redirecionar para a página de boas-vindas após o login bem-sucedido
            .permitAll()
            .and()
            .logout()
            .permitAll();
    }
}



