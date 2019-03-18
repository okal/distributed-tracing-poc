package heavy;


import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class ResultController {
    @RequestMapping("/result")
    public Result result() {
        return new Result("ola");
    }
}